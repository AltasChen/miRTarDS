import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc, precision_recall_curve, f1_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from ast import literal_eval
import time

start = time.time()

# file path
file_paths = ['miRTarDS_combined.txt']

def calculate_metrics(file_path, num_samples=100):

    original_data = pd.read_csv(file_path, sep='\t')

    original_data = original_data.drop('miRTarDS Prediction', axis=1)
    
    def update_exp(value):

        if 'Functional MTI' in value and 'Weak' not in value and 'Non' not in value:
            return 'Strong Interaction'
        elif 'Functional MTI (Weak)' in value:
            return 'Weak Interaction'
        elif 'Non-Functional MTI' in value and 'Weak' not in value:
            return 'Strong No Interaction'
        elif 'Non-Functional MTI (Weak)' in value:
            return 'Weak No Interaction'
        else:
            return 'Prediction Interaction'
        
    original_data['Support Type'] = original_data['Support Type'].apply(update_exp)

    functional_mti_count = original_data[original_data['Support Type'] == 'Strong Interaction'].shape[0]

    miRWalk_rows = original_data[original_data['Support Type'] == 'Prediction Interaction']
    random_miRWalk_rows = miRWalk_rows.sample(n=functional_mti_count, random_state=None)

    data = pd.concat([original_data[original_data['Support Type'] == 'Strong Interaction'], random_miRWalk_rows])
    
    data['Hist'] = data['Hist'].apply(literal_eval)

    data = data[data['Hist'].apply(lambda x: x != [0, 0, 0, 0, 0])]
    
    data['Hist'] = data['Hist'].apply(lambda x: [round(i/sum(x), 4) for i in x])

    X = data['Hist'].tolist()
    y = data['Support Type'].tolist()

    y = [0 if label == 'Strong Interaction' else 1 for label in y]

    X = pd.DataFrame(X)

    models = {
        'Random Forest': RandomForestClassifier()
    }

    metrics = {name: {'f1_scores': [], 'precision_scores': [], 'recall_scores': []} for name in models}
    
    roc_values = {'fpr': [], 'tpr': [], 'auc': 0}
    prc_values = {'precision': [], 'recall': [], 'auc': 0}
    
    cumulative_cm = np.zeros((2, 2), dtype=int)

    best_f1_score = -1
    best_model = None
    best_model_name = ""

    for _ in range(num_samples):

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None)

        for name, model in models.items():

            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            f1 = f1_score(y_test, y_pred, pos_label=0)
            precision_score_value = precision_score(y_test, y_pred, pos_label=0, zero_division=0)
            recall = recall_score(y_test, y_pred, pos_label=0)

            metrics[name]['f1_scores'].append(f1)
            metrics[name]['precision_scores'].append(precision_score_value)
            metrics[name]['recall_scores'].append(recall)

            if f1 > best_f1_score:
                best_f1_score = f1
                best_model = model
                best_model_name = name

            cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
            cumulative_cm += cm

            if name == 'Random Forest':

                y_probs = model.predict_proba(X_test)[:, 0]

                # ROC
                fpr, tpr, _ = roc_curve(y_test, y_probs, pos_label=0)
                roc_values['fpr'].append(fpr)
                roc_values['tpr'].append(tpr)
                roc_auc = auc(fpr, tpr)
                roc_values['auc'] += roc_auc

                # PRC
                precision, recall, _ = precision_recall_curve(y_test, y_probs, pos_label=0)
                prc_values['precision'].append(precision)
                prc_values['recall'].append(recall)
                prc_auc = auc(recall, precision)
                prc_values['auc'] += prc_auc

    # if best_model is not None:
    #     model_filename = f"Best_Model_{best_model_name.replace(' ', '_')}.pkl"
    #     joblib.dump(best_model, model_filename)

    roc_values['auc'] /= num_samples
    prc_values['auc'] /= num_samples

    plt.figure(figsize=(8, 6), dpi=300)
    for fpr, tpr in zip(roc_values['fpr'], roc_values['tpr']):
        plt.plot(fpr, tpr, color='#2170b4', alpha=0.1, linewidth=0.8)
    plt.plot([0, 1], [0, 1], color='grey', linestyle='--', linewidth=1)
    plt.title(f'ROC Curve (AUC = {roc_values["auc"]:.4f})', fontsize=14)
    plt.xlabel('False Positive Rate', fontsize=12) 
    plt.ylabel('True Positive Rate', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6) 
    plt.tight_layout()  
    plt.savefig('ROC_RF', bbox_inches='tight') 

    plt.figure(figsize=(8, 6), dpi=300)
    for precision, recall in zip(prc_values['precision'], prc_values['recall']):
        plt.plot(recall, precision, color='#2170b4', alpha=0.1, linewidth=0.8) 
    plt.title(f'PRC Curve (AUC = {prc_values["auc"]:.4f})', fontsize=14) 
    plt.xlabel('Recall', fontsize=12)
    plt.ylabel('Precision', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)  
    plt.tight_layout()  
    plt.savefig('PRC_RF', bbox_inches='tight')  

    average_cm = cumulative_cm / num_samples

    plt.figure(figsize=(8, 6))
    sns.heatmap(average_cm, annot=True, fmt='.2f', cmap='Blues', xticklabels=['Strong Interaction', 'Prediction Interaction'], yticklabels=['Strong Interaction', 'Prediction Interaction'])
    plt.title(f'Average Confusion Matrix for Random Forest', fontsize=16)
    plt.xlabel('Predicted Label', fontsize=14)
    plt.ylabel('True Label', fontsize=14)
    plt.savefig('Average_Confusion_Matrix_RF.png')

    results = {}
    for name in models:
        mean_f1 = np.mean(metrics[name]['f1_scores'])
        mean_precision = np.mean(metrics[name]['precision_scores'])
        mean_recall = np.mean(metrics[name]['recall_scores'])
        results[name] = (mean_f1, mean_precision, mean_recall)

    return results

for file_path in file_paths:
    results = calculate_metrics(file_path)
    print(f"Metrics for {file_path}:")
    for model_name, (mean_f1, mean_precision, mean_recall) in results.items():
        print(f"{model_name}:")
        print(f"  Average F1 score: {mean_f1:.3f}")
        print(f"  Average Precision: {mean_precision:.3f}")
        print(f"  Average Recall: {mean_recall:.3f}")
    print()

        
end = time.time()
runtime_seconds = end - start 
hours, remainder = divmod(runtime_seconds, 3600)  
minutes, seconds = divmod(remainder, 60)
print(f'Running Time: {hours} hours, {minutes} minutes, {seconds} seconds')
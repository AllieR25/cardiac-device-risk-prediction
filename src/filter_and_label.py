import pandas as pd

def load_data():
    # Load raw data files
    maudevent = pd.read_csv('data/raw/maudevent/maudevent.txt', sep='|', dtype=str, low_memory=False)
    foidev = pd.read_csv('data/raw/foidev/foidev.txt', sep='|', dtype=str, low_memory=False)
    foitext = pd.read_csv('data/raw/foitext/foitext.txt', sep='|', dtype=str, low_memory=False)
    return maudevent, foidev, foitext

def merge_and_filter(maudevent, foidev, foitext):
    # Merge device and narrative text data on report key
    device_text = pd.merge(foidev, foitext, on='MDR_REPORT_KEY', how='left')

    # Merge with event metadata for labels
    full_data = pd.merge(device_text, maudevent[['MDR_REPORT_KEY', 'EVENT_TYPE']], on='MDR_REPORT_KEY', how='left')

    # Filter for cardiac devices by DEVICE_NAME keyword
    cardiac_mask = full_data['DEVICE_NAME'].str.contains('pacemaker|defibrillator', case=False, na=False)
    cardiac_data = full_data[cardiac_mask].copy()

    # Optional: map EVENT_TYPE to severity labels
    severity_map = {
        'Death': 'Severe',
        'Injury': 'Severe',
        'Malfunction': 'Moderate',
        'Other': 'Mild'
    }
    cardiac_data['SEVERITY_LABEL'] = cardiac_data['EVENT_TYPE'].map(severity_map).fillna('Unknown')

    return cardiac_data

def save_filtered_data(df):
    df.to_csv('data/processed/cardiac_events_filtered.csv', index=False)
    print(f"Saved filtered data with {len(df)} records to data/processed/cardiac_events_filtered.csv")

def main():
    maudevent, foidev, foitext = load_data()
    cardiac_data = merge_and_filter(maudevent, foidev, foitext)
    save_filtered_data(cardiac_data)

if __name__ == '__main__':
    main()

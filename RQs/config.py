GPT4O_RESULTS_DIR = 'normalized_PII_results/gpt4o/db_level/'
GROUND_TRUTH_DIR = 'normalized_PII_results/ground_truth/db_level/'

PII_TYPES = ['EMAIL', 'PHONE', 'USERNAME', 'PERSON_NAME', 'POSTAL_ADDRESS']

APP_MAPPING = {
    'A1': 'WhatsApp',
    'A2': 'Snapchat',
    'A3': 'Telegram',
    'A4': 'Google Maps',
    'A5': 'Samsung Internet',
    'I1': 'WhatsApp (iOS)',
    'I2': 'Contacts',
    'I3': 'Apple Messages',
    'I4': 'Safari',
    'I5': 'Calendar'
}

COLUMN_MAPPING = {
    'EMAIL': 'Email',
    'PHONE': 'Phone',
    'USERNAME': 'User Name',
    'PERSON_NAME': 'Person Name',
    'POSTAL_ADDRESS': 'Postal Address'
}

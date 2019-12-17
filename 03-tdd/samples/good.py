import json
import pandas as pd
from datetime import datetime


def read_data(path):
    with open(path, 'r') as f:
        return json.load(f)


def generate_dataset(data):
    return pd.DataFrame(data, columns=['Name', 'Age'])


def clean_dataset(df):
    df['fake'] = df['Age'] + 18
    df['datetime'] = datetime.now()
    # ...
    return df


def split():
    train_data, validate_data = split(df)
    return train_data, validate_data


def train_model(train_data):
    model = MyAwesomeModel()
    model.train(train_data)
    return model


def validate_model(validate_data):
    score = model.validate(validate_data)
    if score.score > 0.75:
        return {'recall': score.sensibility, 'precision': score.precision, 'accuracy': score.accuracy, 'datetime': datetime.now()}
    return {'error': score.error, 'datetime': datetime.now()}


def upload_results(score):
    table_service = TableService()
    table_service.push(score)


if __name__ == "__main__":
    data = read_data('path/to/glory.json')
    df = generate_dataset(data)
    df = clean_dataset(df)
    train_data, validate_data = split()
    model = train_model(train_data)
    score = validate_model(validate_data)
    upload_results(score)

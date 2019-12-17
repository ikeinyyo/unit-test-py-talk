import json
import pandas as pd
from datetime import datetime


def do_a_lot_of_thinks():
    # Read data
    with open('path/to/defeat.py', 'r') as f:
        data = json.load(f)

    # Create dataset
    df = pd.DataFrame(data, columns=['Name', 'Age'])

    # Clean dataset
    df['fake'] = df['Age'] + 18
    df['datetime'] = datetime.now()
    # ...

    # split
    train_data, validate_data = split(df)

    # train
    model = MyAwesomeModel()
    model.train(train_data)

    # validate
    score = model.validate(validate_data)
    if score.score > 0.75:
        score_data = {'recall': score.sensibility, 'precision': score.precision,
                      'accuracy': score.accuracy, 'datetime': datetime.now()}
    else:
        score_data = {'error': score.error, 'datetime': datetime.now()}

    table_service = TableService()
    table_service.push(score_data)


if __name__ == "__main__":
    do_a_lot_of_thinks()

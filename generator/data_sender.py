import time
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import psycopg2


def send_data():
    conn = psycopg2.connect(
        host="localhost", database="sales", user="iwd", password="iwd@2022"
    )

    while True:
        try:
            time.sleep(1)
            cursor = conn.cursor()
            dt = datetime.now(timezone.utc)
            cursor.execute(
                "INSERT INTO clicks (ts, product_id) VALUES (%s, %s)",
                (dt, np.random.randint(1, 5)),
            )
            cursor.execute(
                "INSERT INTO sales (ts, product_id, price) VALUES (%s, %s, %s)",
                (dt, np.random.randint(1, 5), np.random.normal(50, 20)),
            )
            conn.commit()
            cursor.close()

        except KeyboardInterrupt:
            conn.close()
            exit()


if __name__ == "__main__":
    send_data()

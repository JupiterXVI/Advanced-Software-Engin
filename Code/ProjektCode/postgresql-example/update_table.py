#!/usr/bin/python

import psycopg2
from config import config


def update_vendor(vendor_id, vendor_name):
    """ update vendor name based on the vendor id """

    sql = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s """

    conn = None
    update_row = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE statement
        cur.execute(sql, (vendor_name, vendor_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # commit the changes to the database
        conn.commit()
        # close communikation with the PostgreSQL databas
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    # update vendor with id 1
    update_vendor(18, '3M Corp')
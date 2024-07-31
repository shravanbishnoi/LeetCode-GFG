import psycopg2

POSTGRES_HOST = ""
POSTGRES_DB = ""
POSTGRES_USER = ""
POSTGRES_PASSWORD = ""

# creating tables for storing different category of articles for my newsAPP

categories=['business','entertainment','health','science','sports','technology',
            'education', 'general', 'domestic', 'environment', 'food', 'lifestyle',
            'politics', 'top', 'tourism', 'world', 'nation', 'other', 'crime']


def create_tables(table_names):
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
        cur = conn.cursor()

        create_table_command = '''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            summary TEXT,
            published TIMESTAMP,
            imageURL TEXT,
            source TEXT,
            score REAL,
            adverb_count INTEGER,
            adjective_count INTEGER,
            noun_count INTEGER,
            pronoun_count INTEGER,
            verb_count INTEGER,
            apiname TEXT
        );
        '''

        for table_name in table_names:
            formatted_command = create_table_command.format(table_name=table_name)
            cur.execute(formatted_command)
        
        conn.commit()

        cur.close()
        conn.close()

        print("Tables created successfully")

    except Exception as e:
        print(f"Error creating tables: {e}")

create_tables(categories)

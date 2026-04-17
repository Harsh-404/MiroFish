import neo4j

# Function to initialize Neo4j connection
def init_neo4j_connection(uri, user, password):
    driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))
    return driver

# Function to migrate data

def migrate_data(src_data):
    # Assume src_data is a list of dictionaries
    with driver.session() as session:
        for record in src_data:
            session.run("CREATE (n:Node {props})", props=record)

# Main migration function

def main():
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"
    driver = init_neo4j_connection(uri, user, password)
    # Example of source data
    src_data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ]
    migrate_data(src_data)
    driver.close()

if __name__ == '__main__':
    main()
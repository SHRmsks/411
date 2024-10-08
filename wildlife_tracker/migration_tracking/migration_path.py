from typing import Optional

class MigrationPath:
    def __init__(self, migration_path: MigrationPath,) -> None:
        self.migration_path = migration_path
        pass
    

    def get_migration_path_by_id(path_id: int) -> MigrationPath:
        pass
    
    def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
        pass
        
    
    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
        pass
    def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
        pass
    def get_migrations_by_current_location(current_location: str) -> list[Migration]:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
        pass
    def get_migration_path_details(path_id) -> dict:
        pass
    
    def remove_migration_path(path_id: int) -> None:
        pass
    


    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass
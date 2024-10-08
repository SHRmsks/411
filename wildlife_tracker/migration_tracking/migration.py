from typing import Any

class Migration:
    def __init__(self,  current_date: str, migration_id: int,
        destination: Habitat, 
         start_location: Habitat, current_location: str, 
        species: str,
         path_id: int,
          start_date: str,
        status: str = "Scheduled",
        paths: dict[int, MigrationPath] = {},
         duration: Optional[int] = None,

       ) -> None:
        self.current_date =current_date
        self.start_date = start_date
        self.migration_id = migration_id
        self.start_location = start_location
        self.path_id = path_id
        self.species = species
        self.destination =destination
        self.current_location= current_location
        self.status = status 
        self.paths =paths
        self.duration = duration
        pass
    def get_migration_paths() -> list[MigrationPath]:
        pass
  
   
    
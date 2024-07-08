import fs

def create_directory_if_not_exists(fs_object: OSFS, path: str) -> OSFS:
    """Ensure the directory exists; create it if it doesn't.
    
    Args:
    - fs (OSFS): An OSFS object representing the file system.
    
    Returns:
    - OSFS: The OSFS object representing the file system.
    """
    return fs_object.makedir(path) if not fs_object.exists(path) else fs_object.opendir(path)
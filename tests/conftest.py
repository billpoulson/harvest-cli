import os
import tempfile
import uuid

import pytest

@pytest.fixture(scope="module")
def temp_config_filex():
    temp_file_path = os.path.join(tempfile.gettempdir(), f".test_{uuid.uuid4()}.json")

    print(f'yielding config file path: {temp_file_path}')
    yield temp_file_path
    
    print('cleaning up files')
    
    # Cleanup: Remove the temporary config file if it exists
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
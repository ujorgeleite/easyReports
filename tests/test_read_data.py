import pytest
import pandas as pd
from datetime import datetime
from src.modules.read_data import ReadData  # Adjust this import to match your project's structure

# Sample data for testing
sample_data = {
    "DATA": ["2024-01-05", "2024-06-15", "2024-12-30", "2023-12-25"],
    "VALOR": [100, 200, 300, 400],
    "UF": ["SP", "RJ", "MG", "BA"],
}

# Fixture to create a sample DataFrame for testing
@pytest.fixture
def sample_df():
    return pd.DataFrame(sample_data)

# Fixture to create an instance of ReadData for testing
@pytest.fixture
def read_data():
    return ReadData(file_path="dummy_path.xlsx")

def test_filter_by_date_range(read_data, sample_df):
    # Define start and end dates in the ReadData instance
    read_data.start_date = "2024-01-01"
    read_data.end_date = "2024-12-31"
    
    # Filter by date and verify results
    filtered_df = read_data.filter_by_date_range(sample_df, "DATA")
    expected_data = sample_df[(sample_df["DATA"] >= "2024-01-01") & (sample_df["DATA"] <= "2024-12-31")]

    assert len(filtered_df) == len(expected_data)
    assert filtered_df["DATA"].equals(expected_data["DATA"])

def test_filter_by_date_range_no_data_in_range(read_data, sample_df):
    # Test with a date range outside any dates in the sample data
    read_data.start_date = "2025-01-01"
    read_data.end_date = "2025-12-31"
    
    filtered_df = read_data.filter_by_date_range(sample_df, "DATA")
    
    assert filtered_df.empty  # No rows should match this range

def test_read_and_select_columns(monkeypatch, read_data, sample_df):
    # Mock pd.read_excel to return sample_df
    def mock_read_excel(*args, **kwargs):
        return sample_df
    
    monkeypatch.setattr(pd, "read_excel", mock_read_excel)
    
    selected_columns = ["DATA", "VALOR"]
    result_df = read_data.read_and_select_columns(sheet_name="Sheet1", columns=selected_columns)
    
    assert isinstance(result_df, pd.DataFrame)
    assert list(result_df.columns) == selected_columns

def test_read_and_select_columns_file_not_found(read_data,capsys):
    # Set up with a non-existent file path
    read_data.file_path = "non_existent_file.xlsx"
    read_data.read_and_select_columns(sheet_name="Sheet1", columns=["DATA", "VALOR"])
    captured = capsys.readouterr()
    
    # Assert the printed error message
    assert "Error: The file non_existent_file.xlsx does not exist." in captured.out

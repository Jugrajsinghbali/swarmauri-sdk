import pytest
from swarmauri.standard.tools.concrete.TextLengthTool import TextLengthTool as Tool

@pytest.mark.unit
def test_ubc_resource():
    tool = Tool()
    assert tool.resource == 'Tool'

@pytest.mark.unit
def test_ubc_type():
    assert Tool().type == 'TextLengthTool'

@pytest.mark.unit
def test_initialization():
    tool = Tool()
    assert type(tool.id) == str

@pytest.mark.unit
def test_call(): 
    tool = Tool()
    text = "This is a simple test sentence."
    result = tool(text)

    assert result["num_characters"] == 26
    assert result["num_words"] == 7
    assert result["num_sentences"] == 1 

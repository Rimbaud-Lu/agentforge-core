from skills.code.generate_api import generate_api

def test_generate_api():
    result = generate_api("test")
    
    assert "created" in result

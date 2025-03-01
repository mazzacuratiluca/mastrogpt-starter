import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/lmazzacurati/reverse"
    var = "test"
    args = {"input": var}
    res = req.get(url,args).json()
    assert res.get("output") == var[::-1]

    args = {'input': "" }
    res = req.get(url,args).json()
    assert res.get("output") == "Plese provide some input"

import sys 
sys.path.append("packages/lmazzacurati/reverse")
import reverse

def test_reverse():
    var = "test"
    args = {'input': var }
    res = reverse.reverse(args)
    assert res["output"] == var[::-1]

    args = {'input': "" }
    res = reverse.reverse(args)
    assert res["output"] == "Plese provide some input"

## Test Execution

1. **From the root file of the proyect `/practica_os` execute each test with the following commands:**
ProdCons Test Basic
```bash
python -m unittest discover -s test -p "prod_cons_test_basic.py"
```

ProdCons Test Sync
```bash
python -m unittest discover -s test -p "prod_cons_test_sync.py"
```

RendezVous Test Basic
```bash
python -m unittest discover -s test -p "rendezvous_test_basic.py"
```

ProdCons Test Sync
```bash
python -m unittest discover -s test -p "rendezvous_test_sync.py"
```

All tests
```bash
python -m unittest discover -s test -p "*.py"
```

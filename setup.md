# Creación de un entorno venv para scripts
python3.9 -m venv venv

## Activación de ambiente virtual
source venv/bin/activate

## Instalación de dependencias
pip install -r requirements.txt

## Ejecutar scripts
diferencias_np_pd.py

python generator.py

### Manual Testing*
python calculadora.py suma 5 3

### Test Automation
python ejm_unittest.py
pytest ejm_pytest.py
pytest ejm_hypothesis.py
pytest ejm_hypothesis_nan.py

python ejm_pydantic.py
python ejm_pandera.py
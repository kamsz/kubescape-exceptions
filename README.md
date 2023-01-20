# kubescape-exceptions

A simple Python script to generate exceptions JSON used in [Kubescape](https://github.com/kubescape/kubescape).

Please keep in mind that `build_json.py` should be adjusted to match your infrastructure.

## How to use?

In order to generate the JSON simply run:

```python
python build_json.py > kubescape-exceptions.json
```

And include this file while running Kubescape:

```bash
kubescape scan --exceptions kubescape-exceptions.json -v
```

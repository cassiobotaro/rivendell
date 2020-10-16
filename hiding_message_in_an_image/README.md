# Hiding message in an image

# Step 1 - Create virtual environment

```bash
python -m venv .venv && source .venv/bin/activate
```

# Step 2 - Install Dependencies

```bash
python -m pip install stegano
```

# Step 3 - Hiding image

```bash
stegano-lsb hide -i ./tests/sample-files/Lenna.png -m "Secret Message" -o Lena1.png
```

# Step 4 - To reveal image execute:

```bash
stegano-lsb reveal -i Lena1.png
```

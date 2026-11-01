# Hiding message in an image

# Step 1 - Hiding image

```bash
uvx --from stegano stegano-lsb hide -i ./cv/lena.jpg -m "Secret Message" -o lena1.png
```

# Step 2 - To reveal image execute:

```bash
uvx --from stegano stegano-lsb reveal -i lena1.png
```

# Note - Messages with accents (non-ASCII)

Stegano 3.x hides and reveals accented messages as UTF-8 out of the box:

```bash
uvx --from stegano stegano-lsb hide -i ./cv/lena.jpg -m "Às vezes... você" -o lena2.png
uvx --from stegano stegano-lsb reveal -i lena2.png
```

Images produced by older versions or other tools may store the text as
Latin-1 (one byte per character). For those, `reveal` fails with
`Impossible to detect message.` Decode them as Latin-1 instead:

```bash
uvx --from stegano python -c "
from stegano import lsb, tools
tools.ENCODINGS['latin-1'] = 8
print(lsb.reveal('lena1.png', encoding='latin-1'))"
```

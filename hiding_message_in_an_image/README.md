# Hiding message in an image

# Step 1 - Hiding image

```bash
uvx --from stegano stegano-lsb hide -i ./cv/lena.jpg -m "Secret Message" -o lena1.png
```

# Step 2 - To reveal image execute:

```bash
uvx --from stegano stegano-lsb reveal -i lena1.png
```

(common-issues)=

# Common Issues

## Permissions

### Description

You encounter "Permission denied" errors when trying to read, write, or execute files or directories. This typically occurs when you do not own the file or folder, or when the proper group read/write privileges have not been granted.

### Steps to Resolve

1. Determine who owns the file or directory by running:
   ```bash
   ls -l /path/to/file
   ```
2. **If you are the owner**:
   Restore standard group privileges by running:
   ```bash
   ensure_permissions /path/to/file
   ```
3. **If you are not the owner**:
   Ask the file's owner to run the `ensure_permissions` command shown above.
4. **If the owner is a numeric UID instead of a NetID**:
   Contact {{cvltech}} for administrator assistance.

## End of Line Sequence (CRLF vs LF)

### Description

When executing scripts on the server, you receive error messages similar to:

```text
line 1: $':\r': command not found
line 5: syntax error near unexpected token `$'\r''
```

This error signifies that the file contains Windows-style carriage return line endings (`CRLF`) instead of Unix-style line endings (`LF`). This typically happens when code is written or copy-pasted from Windows applications, text editors, or web browsers.

### Steps to Resolve

#### Option A: Using the `vi` Text Editor (in Terminal)
1. Open the file in the terminal using `vi`'s binary mode:
   ```bash
   vi -b /path/to/file
   ```
2. Strip the carriage returns (`\r`) by typing the following command in `vi` and pressing `Enter`:
   ```bash
   :%s/\r$//
   ```
3. Save the changes and exit by typing `:x` and pressing `Enter`.

#### Option B: Using the `nano` Text Editor (in Terminal)
1. Open the file in the terminal:
   ```bash
   nano /path/to/file
   ```
2. Press `Ctrl+O` to initiate writing out (saving) the file.
3. At the filename prompt, press `Alt+D` (on macOS, press `Esc` then `D`) to toggle the DOS format off. You will see `[DOS Format]` disappear from the status bar.
4. Press `Enter` to confirm saving the file in Unix format.
5. Press `Ctrl+X` to exit.

#### Option C: Using Visual Studio Code
If you are testing scripts that read from a `.csv` file and find the terminal output is cut off or flipped, the `.csv` is likely saved in Windows-style format.
1. Open the file in Visual Studio Code.
2. Look at the bottom-right status bar, click on **CRLF**, and change it to **LF**.
3. Save the file.

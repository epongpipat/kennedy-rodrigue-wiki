(server-configuration)=

# Configuration

## Profiles

Consider adding these global lab profiles to your user profile. You can copy and paste either into its respective profile file by using the `nano` function (e.g., `nano ~/.bash_profile`)

1. `~/.bash_profile`

```bash
if [[ ${HOSTNAME} =~ 'cvlkrcompute' ]]; then
  export root_dir='/cvl/kenrod'
else
  export root_dir='/mfs/cvl/groups/kenrod'
fi
source ${root_dir}/server/profiles/global/bash_profile.sh
```

2. `~/.Rprofile`

```R
if (Sys.info()[['nodename']] == 'cvlkrcompute1.utdallas.edu') {
        root_dir <- '/cvl/kenrod'
} else {
        root_dir <- '/mfs/cvl/groups/kenrod'
}
source(sprintf('%s/server/profiles/global/r_profile.R', root_dir))
```

(passwordless-ssh-login)=
## Passwordless SSH Login

:::{note}
Passwordless SSH are for Mac users. Windows users using Putty/MobaXterm should configure key-based authentication through those applications.
:::

You can set up your system to log in to the server via SSH without typing your password every time.

:::{note}
Generating an SSH key pair (`ssh-keygen`) only needs to be done once per computer.
:::

1. **Generate SSH Key Pair** (on your local computer):
   Open a terminal and run the following command to generate a key pair. Press `Enter` to accept all defaults (do not enter a passphrase):
   
   ```bash
   ssh-keygen -t ed25519
   ```

2. **Copy the Public Key to the Server** (on your local computer):
   Run the `ssh-copy-id` command on your local computer followed by your server login credentials (replace `<user>` with your NetID and `<hostname>` with your target host, e.g. `cortex.cvl.utdallas.edu`):
   
   ```bash
   ssh-copy-id <user>@<hostname>
   ```

3. **Verify Passwordless Connection**:
   Attempt to connect again. You should be logged in automatically without prompting for a password:
   
   ```bash
   ssh -Y <user>@<hostname>
   ```

(ssh-alias-configuration)=
## SSH Alias Configuration

:::{note}
SSH alias configurations are for Mac users. Windows users using Putty/MobaXterm should configure connection profiles within those applications.
:::

To simplify connecting to the servers, you can configure your SSH client aliases. On your local computer, edit or create `~/.ssh/config` and add the following blocks (replace `<utd-netid>` with your actual NetID):

```text
Host cvlkrcompute1 ponyo
        User <utd-netid>
        Hostname ponyo.utdallas.edu
        IdentityFile ~/.ssh/id_ed25519
        ServerAliveInterval 120

Host cortex
        User <utd-netid>
        Hostname cortex.cvl.utdallas.edu
        IdentityFile ~/.ssh/id_ed25519
        ServerAliveInterval 120
```

Once configured, you can log in to the server by simply running:

```bash
ssh ponyo
```
or
```bash
ssh cortex
```

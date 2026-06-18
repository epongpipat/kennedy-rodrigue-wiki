(login)=

# Login with Command Line Interface ({{CLI}})

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Server: cortex (Recommended)
:shadow: sm
HPC Cluster
**Hostname:** `cortex.cvl.utdallas.edu`
:::

:::{grid-item-card} Server: ponyo (Legacy)
:shadow: sm
Standalone Server
**Hostname:** `cvlkrcompute1.utdallas.edu`
**Alias Hostname:** `ponyo.utdallas.edu`
:::
::::

::::::{tab-set}

:::::{tab-item} macOS
1. Run the `ssh` command in your terminal (replacing `<user>` with your {{UTD}} NetID and `<hostname>` with one of the server hostnames listed above) and press `Enter`:
   ```bash
   ssh -Y <user>@<hostname>
   ```
2. If this is your first time connecting, you will see a warning about host authenticity. Type `yes` and press `Enter` to continue.
3. Type your {{UTD}} NetID password and press `Enter`.

:::{note}
Mac users can configure passwordless login and SSH client aliases to log in by simply typing `ssh cortex` or `ssh ponyo` without entering a password. See the [Passwordless SSH Login](passwordless-ssh-login) and the [SSH Alias Configuration](ssh-alias-configuration) pages for instructions.
:::
:::::

:::::{tab-item} Windows
::::{tab-set}

:::{tab-item} MobaXterm (Recommended)
1. Download and install [MobaXterm Home Edition](https://mobaxterm.mobatek.net/download-home-edition.html).
2. Launch MobaXterm and click on **Session** in the top-left toolbar.
3. Select **SSH** from the session types to configure the connection:
   - **Remote host**: Enter one of the hostnames listed above (e.g., `cortex.cvl.utdallas.edu`).
   - **Specify username**: Check the box and enter your {{UTD}} NetID.
   - **Port**: Leave it as `22`.
4. Click **OK**. A terminal prompt will appear asking for your {{UTD}} password; enter it and press `Enter`.
:::

:::{tab-item} PuTTY
1. Download and install [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).
2. Launch PuTTY and configure the session settings:
   - **Host Name (or IP address)**: Enter `<user>@<hostname>` (e.g., `netid@cortex.cvl.utdallas.edu`).
   - **Port**: Leave it as `22`.
   - **Connection type**: Ensure **SSH** is selected.
3. Click **Open**.
4. If a "PuTTY Security Alert" box pops up (verifying host keys), click **Accept** or **Yes**.
5. Enter your NetID password in the terminal window and press `Enter`.
:::

::::
:::::

::::::

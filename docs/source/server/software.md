(server-software)=

# Software

To see available software, run:

```bash
module avail
```

To load available software, run:

```bash
module load <software>
```

To unload software, run:

```bash
module unload <software>
```

## Containers

We prefer that users run their software environment using our pre-built containers to maintain reproducibility and clean environments. 

If you are running software that uses a container, run the code by prefixing it with `<container-name>-exec <cmd>`:

```bash
module load containers/r/4.2.1
r-exec <cmd>
```

For more details on how to build and run containerized environments, see the [Containers section](../containers/index.md).

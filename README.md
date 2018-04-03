# Brainfuck kernel for Jupyter

Brainfuck kernel is a simple kernel for [Jupyter](http://jupyter.org/).

It has been developed using the [wrapper structure](http://jupyter-client.readthedocs.io/en/stable/wrapperkernels.html) that Jupyter provides.

Each input shows a very rich output including the pointer position and stack snapshot.  

## Installation

Just clone this repo, go inside the root dyrectory and execute:
```$ sudo jupyter kernelspec install brainfuck_kernel/```

```$ ./install.sh```

## Using the Brainfuck kernel
**Notebook**: The *New* menu in the notebook should show an option for the Brainfuck notebook.

**Console**: ```$ jupyter console --kernel brainfuck_kernel```

## Thanks

Thanks to **Jacosro** for providing the [interpreter](https://github.com/jacosro/brainfuck-interpreter).

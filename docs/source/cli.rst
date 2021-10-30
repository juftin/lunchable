##################
Lunchable CLI
##################

******************
Installation
******************

To use lunchable, first install it using pip:

.. code-block:: console

    pip install lunchable


or, if you're using the Splitwise plugin on the CLI:

.. code-block:: console

    pip install lunchable[splitwise]

Install Shell Completion
=========================


bash
###################

.. code-block:: console

    _LUNCHABLE_COMPLETE=bash_source lunchable > ~/.lunchable-complete.bash
    echo "[[ ! -f ~/.lunchable-complete.bash ]] || source ~/.lunchable-complete.bash" >> ~/.bashrc

zsh
###################

.. code-block:: console

    _LUNCHABLE_COMPLETE=zsh_source lunchable > ~/.lunchable-complete.zsh
    echo "[[ ! -f ~/.lunchable-complete.zsh ]] || source ~/.lunchable-complete.zsh" >> ~/.zshrc

******************
Documentation
******************

.. click:: lunchable._cli:cli
   :prog: lunchable
   :nested: full
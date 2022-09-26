# C_function_extract
a python script to extract functions from a C SOURCE FILE


# demo:
## a file:
sal_module_wrapper.c

## its content:
```
#include "sal_module_wrapper.h"

static sal_module_t *g_sal_module = NULL;

int tos_sal_module_register(sal_module_t *module)
{
    if (!g_sal_module) {
        g_sal_module = module;
        return 0;
    }

    return -1;
}

int tos_sal_module_register_default()
{
    g_sal_module = NULL;

    return 0;
}
```
... ... and so forth
## use this script
get_functions('D:/helphelpme/sal_module_wrapper.c'):

## result
```
int tos_sal_module_register(sal_module_t *module)
{
    if (!g_sal_module) {
        g_sal_module = module;
        return 0;
    }

    return -1;
}
```
==========================================================================================
```
int tos_sal_module_register_default()
{
    g_sal_module = NULL;

    return 0;
}
```
==========================================================================================
...... and so forth



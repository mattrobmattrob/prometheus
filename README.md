# prometheus

![Travis CI Status](https://travis-ci.org/mattrobmattrob/prometheus.svg?branch=master)

### Format Objective-C Declarations

Python script to alphabetize import declarations (`#import` & `@import`) and forward declarations (`@class` & `@protocol`) that exist in a block. Specifically written for Objective-C code.

## Usage

### Default Behavior

#### Description
Default behavior takes the result of `git status` and uses the files that were added or modified and subsequently added to be committed and alphabetizes the sections that match the prefixes (either default or passed in via `--prefixes`). The default prefixes are `@import`, `@class`, `#import`, or `@protocol`.

#### Command
```bash
python prometheus
```

#### Example
1. Result of `git status`
```bash
~/CodeExample> git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
(use "git reset HEAD <file>..." to unstage)

new file:   SourceFile.m
```
2. `SourceFile.m` on local filesystem add with `git add`
```Objective-C
#import "Fail.h"
#import "Accept.h"
#import "Category.h"

@class ForwardClass;
@class BackwardClass;
```
3. `SourceFile.m` on local filesystem after running `python prometheus`
```Objective-C
#import "Accept.h"
#import "Category.h"
#import "Fail.h"

@class BackwardClass;
@class ForwardClass;
```

### Branch Based Differencing

#### Description
The branch based differencing method takes the files from the result of `git diff` between the specified branches and alphabetizes the sections in those files that match the prefixes (either default or passed in via `--prefixes`). The default prefixes are `@import`, `@class`, `#import`, or `@protocol`.

#### Command
```bash
python prometheus --compare mr/code.changes
python prometheus --base origin/feature.branch --compare mr/code.changes
```

#### Example
1. `SourceFile.m` doesn't exist on `origin/master`
2. `SourceFile.m` already committed on `mr/code.changes`
```Objective-C
#import "Fail.h"
#import "Accept.h"
#import "Category.h"

@class ForwardClass;
@class BackwardClass;
```
3. `SourceFile.m` on local filesystem after running `python prometheus --base origin/master --compare mr/test.branch` or `python prometheus --compare mr/test.branch`
```Objective-C
#import "Accept.h"
#import "Category.h"
#import "Fail.h"

@class BackwardClass;
@class ForwardClass;
```

### Prefix Overrides

#### Description
The uses either of the previous methods for generating a file list and alphabetizes the sections in those files that match the prefixes passed in via `--prefixes`.

#### Command
```bash
python prometheus --prefixes "import"
python prometheus --prefixes "import" "class"
python prometheus --compare mr/code.changes --prefixes "import"
python prometheus --base origin/feature.branch --compare mr/code.changes --prefixes "import"
```

#### Example
1. `SourceFile.py` doesn't exist on `origin/master`
2. `SourceFile.py` already committed on `mr/code.changes`

```python
import subprocess
import os
import re
import argparse
```

3. `SourceFile.py` on local filesystem after running `python prometheus --compare mr/test.branch --prefixes "import"`
```python
import argparse
import os
import re
import subprocess
```

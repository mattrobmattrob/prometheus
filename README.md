![Travis CI Status](https://travis-ci.org/mattrobmattrob/Format-ObjC-Declarations.svg?branch=master)

### Format Objective-C Declarations

Python script to alphabetize import declarations (`#import` & `@import`) and forward declarations (`@class` & `@protocol`) that exist in a block. Specifically written for Objective-C code.

## Usage

### Default Behavior

#### Description
Default behavior takes the result of `git status` and uses the files that were added or modified and subsequently added to be committed and alphabetizes the sections that match the prefixes (either default or passed in via `--prefixes`). The default prefixes are `@import`, `@class`, `#import`, or `@protocol`.

#### Command
```bash
python FormatHeaders
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
2. `SourceFile.m` on filesystem
  ```Objective-C
  #import "Fail.h"
  #import "Accept.h"
  #import "Category.h"

  @class ForwardClass;
  @class BackwardClass;
  ```
3. `SourceFile.m` on filesystem after running `python FormatHeaders`
  ```Objective-C
  #import "Accept.h"
  #import "Category.h"
  #import "Fail.h"

  @class BackwardClass;
  @class ForwardClass;
  ```

### Branch Based Differencing



### Prefix Overrides

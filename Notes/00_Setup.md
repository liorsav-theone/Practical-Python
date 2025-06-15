# Course Setup and Overview

Welcome to Practical Python Programming!  This page has some important information
about course setup and logistics.

## Course Duration and Time Requirements

This course was originally given as an instructor-led in-person
training that spanned 3 to 4 days.  To complete the course in its
entirety, you should minimally plan on committing 15-25 hours of work.
Most participants find the material to be quite challenging without
peeking at solution code (see below).

## Setup and Python Installation

Almost all necessary tools and libraries for this course have already been installed on
your Ubuntu machine, thanks to the excellent work of our DevOps team, "Fusion".

To install the missing python libraries run the following bash commands:

```bash
pip install pydantic
pip install PyYAML
```

Throughout the course, I recommend using Visual Studio Code along with its
integrated terminal for writing and running Python code.

## Forking/Cloning the Course Repository

To prepare your environment for the course, I recommend creating your
own fork of this course GitLab repo.

## Coursework Layout

Do all of your coding work in the `Work/` directory.  Within that
directory, there is a `Data/` directory.  The `Data/` directory
contains a variety of datafiles and other scripts used during the
course. You will frequently have to access files located in `Data/`.
Course exercises are written with the assumption that you are creating
programs in the `Work/` directory.

## Course Order

Course material should be completed in section order, starting with
section 1.  Course exercises in later sections build upon code written in
earlier sections.  Many of the later exercises involve minor refactoring
of existing code.

## Solution Code

The `Solutions/` directory contains full solution code to selected
exercises.  Feel free to look at this if you need a hint.  To get the
most out of the course however, you should try to create your own
solutions first.

[Contents](Contents.md) \| [Next (1 Introduction to Python)](01_Introduction/00_Overview.md)

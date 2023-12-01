"""CSCA08 Assignment 3: arxiv.org

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021-2023 Anya Tafliovich.

"""

import copy  # needed in examples of functions that modify input dict
from typing import TextIO

# remove unused constants from this import statement when you are
# finished your assignment
from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS,
                       ABSTRACT, END, SEPARATOR, NameType,
                       ArticleValueType, ArticleType, ArxivType)


EXAMPLE_ARXIV = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''},
    '031': {
        'identifier': '031',
        'title': 'Calculus is the best course ever',
        'created': None,
        'modified': '2021-09-02',
        'authors': [('Breuss', 'Nataliya')],
        'abstract': '''We discuss the reasons why Calculus I
is the best course.'''},
    '067': {'identifier': '067',
            'title': 'Discrete Mathematics is the best course ever',
            'created': '2021-09-02',
            'modified': '2021-10-01',
            'authors': [('Bretscher', 'Anna'), ('Pancer', 'Richard')],
            'abstract': ('We explain why Discrete Mathematics is the best ' +
                         'course of all times.')},
    '827': {
        'identifier': '827',
        'title': 'University of Toronto is the best university',
        'created': '2021-08-20',
        'modified': '2021-10-02',
        'authors': [('Bretscher', 'Anna'),
                    ('Ponce', 'Marcelo'),
                    ('Tafliovich', 'Anya Y.')],
        'abstract': '''We show a formal proof that the University of
Toronto is the best university.'''},
    '042': {
        'identifier': '042',
        'title': None,
        'created': '2021-05-04',
        'modified': '2021-05-05',
        'authors': [],
        'abstract': '''This is a very strange article with no title
and no authors.'''}
}

EXAMPLE_BY_AUTHOR = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}

EXAMPLE_A = {
        '080': {
            'identifier': '080',
            'title': 'Music is really cool',
            'created': '2023-12-15',
            'modified': None,
            'authors': [('Leong', 'Tony')],
            'abstract': '''I give conclusive evidence why MY music is
    objectively cool.'''}
        }

EXAMPLE_BA = {
        ('Leong', 'Tony'): ['080']
        }

EXAMPLE_B = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': None,
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''}
    }

EXAMPLE_BB = {}

EXAMPLE_C = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': [('Tafliovich', 'Anya Y.')],
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''},
    '031': {
        'identifier': '031',
        'title': 'Calculus is the best course ever',
        'created': None,
        'modified': '2021-09-02',
        'authors': [('Breuss', 'Nataliya')],
        'abstract': '''We discuss the reasons why Calculus I
is the best course.'''},
    '827': {
        'identifier': '827',
        'title': 'University of Toronto is the best university',
        'created': '2021-08-20',
        'modified': '2021-10-02',
        'authors': [('Bretscher', 'Anna'),
                    ('Ponce', 'Marcelo'),
                    ('Tafliovich', 'Anya Y.')],
        'abstract': '''We show a formal proof that the University of
Toronto is the best university.'''},
        }

EXAMPLE_D = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}

EXAMPLE_BC = {
    'identifier': '008',
    'title': 'Intro to CS is the best course ever',
    'created': '2021-09-01',
    'modified': None,
    'authors': [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
    'abstract': '''We present clear evidence that Introduction to
    Computer Science is the best course.'''
}

EXAMPLE_E = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827', '123', '234'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}

EXAMPLE_F = [
    ('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.'),
    ('Tafliovich', 'Anya Y.'), ('Chakour', 'Adam')
]


# We provide the header and docstring for this function to get you
# started and to demonstrate that there are no docstring examples in
# functions that read from files.
def read_arxiv_file(afile: TextIO) -> ArxivType:
    """Return a dict containing all arxiv information in afile.

    Precondition: afile is open for reading
                  afile is in the format described in the handout
    """

    pass


# We provide the header and part of a docstring for this function to
# get you started and to demonstrate the use of example data.
def make_author_to_articles(
        id_to_article: ArxivType) -> dict[NameType, list[str]]:
    """Return a dict that maps each author name to a list (sorted in
    lexicographic order) of IDs of articles written by that author,
    based on the information in arxiv data id_to_article.

    >>> make_author_to_articles(EXAMPLE_ARXIV) == EXAMPLE_BY_AUTHOR
    True

    >>> make_author_to_articles(EXAMPLE_A) == EXAMPLE_BA
    True
    >>> make_author_to_articles(EXAMPLE_B) == EXAMPLE_BB
    True
    """
    d = {}

    for keys in id_to_article:
        if id_to_article[keys][AUTHORS] is not None:
            for author in id_to_article[keys][AUTHORS]:
                modify_dict(author, keys, d)
    return d


def modify_dict(key: str, value: int, d: dict[str, list[int]]) -> None:
    """Modifies dict 'd' by adding key-values pairs 'key': ['value']
    if key 'key' is not a key in 'd' or appends value 'value' if 'key'
    is defined in 'd'.

    >>> d = {}
    >>> modify_dict('Hello', 41, d)
    >>> d == {'Hello': [41]}
    True
    >>> modify_dict('Hi', 15, d)
    >>> d == {'Hello': [41], 'Hi': [15]}
    True
    >>> modify_dict('Hi', 12, d)
    >>> d == {'Hello': [41], 'Hi': [12, 15]}
    True
    """
    if key not in d:
        d[key] = [value]
    else:
        d[key].append(value)
        d[key].sort()


# ADD DOCSTRINGS!!!
def organize_coauthors(coauthors: list[NameType],
                       author: NameType) -> list[NameType]:
    """Returns a list based off of list 'coauthors', where
    repeated values are only counted once, all instances of
    author 'author' is deleted from the list, and is sorted
    in lexicographic order.

    >>> organize_coauthors(EXAMPLE_F, ('Ponce', 'Marcelo'))
    [('Chakour', 'Adam'), ('Tafliovich', 'Anya Y.')]
    >>> organize_coauthors([], ('Ponce', 'Marcelo'))
    []
    >>> organize_coauthors(EXAMPLE_F, ())
    [('Chakour', 'Adam'), ('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    """
    co_lst = []
    for authors in coauthors:
        if (authors != author) and (authors not in co_lst):
            co_lst.append(authors)
    co_lst.sort()
    return co_lst


def check_list_overlap(lst1: list, lst2: list) -> bool:
    """Return True if and only if at least one element
    in list 'lst1' is also in list 'lst2'.

    >>> check_list_overlap([1, 2], [1, 2, 3])
    True
    >>> check_list_overlap([1, 2], ['a','b', 2])
    True
    >>> check_list_overlap([1, 2], ['a', 'b'])
    False
    >>> check_list_overlap([], [1, 2, 3])
    False
    >>> check_list_overlap([1, 2], [])
    False
    """
    for ele in lst1:
        if ele in lst2:
            return True
    return False


def get_coauthors(id_to_article: ArxivType,
                  author: NameType) -> list[NameType]:
    """Return a list of author names who are coauthors of the author
    specified in 'author', based on the information in arxiv data
    'id_to_article'. (Two people are coauthors if they are authors
    of the same article.) The list is sorted in lexicographic order.

    >>> get_coauthors(EXAMPLE_ARXIV, ('Tafliovich', 'Anya Y.'))
    [('Bretscher', 'Anna'), ('Ponce', 'Marcelo')]
    >>> get_coauthors(EXAMPLE_ARXIV, ('Bretscher', 'Anna'))
    [('Pancer', 'Richard'), ('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    >>> get_coauthors(EXAMPLE_ARXIV, ('Chakour','Adam'))
    []
    """

    author_dict = make_author_to_articles(id_to_article)
    coauthor_list = []

    if author in author_dict:
        for authors in author_dict.items():
            if check_list_overlap(authors[1], author_dict[author]):
                coauthor_list.append(authors[0])

    return organize_coauthors(coauthor_list, author)


def get_most_published_authors(id_to_article: ArxivType) -> list[NameType]:
    """Returns a list of authors who published the most articles,
    based on the information in arxiv data 'id_to_article'.
    (The list has more than one author only in case of a tie,
    and is also sorted in lexicographic order.)
    >>> get_most_published_authors(EXAMPLE_ARXIV)
    [('Bretscher', 'Anna'), ('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    >>> get_most_published_authors(EXAMPLE_B)
    []
    >>> get_most_published_authors(EXAMPLE_C)
    [('Tafliovich', 'Anya Y.')]
    """
    author_dict = make_author_to_articles(id_to_article)
    most_published = 0
    author_lst = []

    for author in author_dict.items():
        if len(author[1]) >= most_published:
            author_lst.append(author[0])
            most_published = len(author[1])
    author_lst.sort()
    return author_lst


def suggest_collaborators(id_to_article: ArxivType,
                          author: NameType) -> list(NameType):
    """Return a list of suggested authors for author 'author' to collaborate
    with. An author is considered a good suggestion, if they are a coauthor of
    a coauthor of 'author', based based on the information in arxiv data
    'id_to_article'. Authors are not to repeated in the list and cannot include
    'author'.

    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Pancer', 'Richard'))
    [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Tafliovich', 'Anya Y.'))
    [('Pancer', 'Richard')]
    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Chakour', 'Adam'))
    []
    """

    suggested_collab = []
    coauthor_lst = get_coauthors(id_to_article, author)

    for coauthor in coauthor_lst:
        new_lst = get_coauthors(id_to_article, coauthor)
        for authors in new_lst:
            if authors not in coauthor_lst:
                suggested_collab.append(authors)
    return organize_coauthors(suggested_collab, author)


def has_prolific_authors(author_to_ids: dict[NameType, list[str]],
                         id_info: ArticleType, prolific_num: int) -> bool:
    """Return True if and only if the article 'id_info' has at least one author
    who is considered prolific. An author is considered prolific if and only if
    the author(s) of article 'id_info' has published at least 'prolific_num'
    articles, which is determined by the dict 'author_to_ids', which maps
    author name to a list of IDs of articles published by that author.

    Precondition: Every author of 'id_info' appears as a key in 'author_to_ids'

    >>> has_prolific_authors(EXAMPLE_D, EXAMPLE_ARXIV['008'], 2)
    True
    >>> has_prolific_authors(EXAMPLE_D, EXAMPLE_ARXIV['031'], 2)
    False
    >>> has_prolific_authors(EXAMPLE_E, EXAMPLE_ARXIV['008'], 4)
    True
    """

    for author in id_info[AUTHORS]:
        if len(author_to_ids[author]) >= prolific_num:
            return True
    return False
# We provide the header and part of a docstring for this function to
# get you started and to demonstrate the use of function deepcopy in
# examples that modify input data.


def keep_prolific_authors(id_to_article: ArxivType,
                          min_publications: int) -> None:
    """Update the articles data id_to_article so that it contains only
    articles published by authors with min_publications or more
    articles published. As long as at least one of the authors has
    min_publications, the article is kept.

    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 2)
    >>> len(arxiv_copy)
    3
    >>> '008' in arxiv_copy and '067' in arxiv_copy and '827' in arxiv_copy
    True
    """

    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod()

    # uncomment to test with example data files
    # with open('example_data.txt', encoding='utf-8') as example_data:
    #     RESULT = read_arxiv_file(example_data)
    #     print('Did we produce a correct dict? ',
    #           RESULT == EXAMPLE_ARXIV)

    # # uncomment to work with a larger data set
    # with open('data.txt', encoding='utf-8') as data_txt:
    #     EXAMPLE = read_arxiv_file(data_txt)

    # EXAMPLE_AUTHOR_TO_ARTICLE = make_author_to_articles(EXAMPLE)
    # EXAMPLE_MOST_PUBLISHED = get_most_published_authors(EXAMPLE)
    # print(EXAMPLE_MOST_PUBLISHED)
    # print(get_coauthors(EXAMPLE, ('Varanasi', 'Mahesh K.')))  # one
    # print(get_coauthors(EXAMPLE, ('Chablat', 'Damien')))  # many

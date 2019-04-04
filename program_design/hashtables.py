# Define a procedure, hashtable_get_bucket,
# that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the
# keyword could occur.


def hashtable_get_bucket(htable, keyword):
    return htable[hash_string(keyword, len(htable))]


def hash_string(keyword, buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out


def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table


def hashtable_add(htable, key, value):
    hashtable_get_bucket(htable, key).append([key, value])


def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for k, v in bucket:
        if key is k:
            return v
    return None


def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for k, v in bucket:
        if key is k:
            return v
    return None


def test():
    assert make_hashtable(2) == [[], []]

    table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
                                                    ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

    assert hashtable_get_bucket(table, "Zoe") == [['Bill', 17], ['Zoe', 14]]

    assert hashtable_get_bucket(table, "Brick") == []

    assert hashtable_get_bucket(table, "Lilith") == [
        ['Louis', 29], ['Rochelle', 4], ['Nick', 2]]
    hashtable_add(table, 'test', 15)
    print(hashtable_get_bucket(table, 'test'))
    print(hash_string('testa', 10))
    assert hashtable_lookup(table, 'Coach') == 4
    print('pass test')


test()

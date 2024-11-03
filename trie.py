def matching_prefix_index(word1, word2):
    max_len = min(len(word1), len(word2))
    for i in range(max_len):
        if word2[i] != word1[i]:
            return i
    return max_len


class PatriciaTrie(object):
    def __init__(self):
        self._storage = {}
        self._complete_prefix_flag = False

    def __contains__(self, word):
        return self.find(word)

    def _find_storage_key(self, word):
        for key in self._storage:
            prefix_index = matching_prefix_index(key, word)
            if prefix_index > 0:
                return (key, prefix_index)
        return (None, None)

    def find(self, word):
        if word == "":
            return self._complete_prefix_flag

        key, prefix_index = self._find_storage_key(word)
        if key is None or prefix_index != len(key):
            return False
        else:
            return word[prefix_index:] in self._storage[key]

    def add(self, word):
        if word == "":
            self._complete_prefix_flag = True
            return True

        key, prefix_index = self._find_storage_key(word)
        if key is not None:
            if prefix_index == len(key):
                return self._storage[key].add(word[len(key) :])
            else:
                new_tree = PatriciaTrie()
                new_tree._storage[key[prefix_index:]] = self._storage.pop(key)
                self._storage[key[0:prefix_index]] = new_tree
                return new_tree.add(word[prefix_index:])
        else:
            self._storage[word] = PatriciaTrie()
            self._storage[word].add("")
            return True

    def remove(self, word):
        if word == "":
            self._complete_prefix_flag = False
            return True

        key, prefix_index = self._find_storage_key(word)
        if key is None or prefix_index != len(key):
            return False

        subword = word[prefix_index:]
        subtrie = self._storage[key]
        if subtrie.remove(subword):
            if (not subtrie._complete_prefix_flag) and len(subtrie._storage) == 0:
                self._storage.pop(key)
            return True
        else:
            return False

    def has_prefix(self, word):
        if word == "":
            return True

        key, prefix_index = self._find_storage_key(word)
        if key is None:
            return False
        elif len(key) > len(word):
            return prefix_index == len(word)
        elif len(key) != prefix_index:
            return False
        else:
            return self._storage[key].has_prefix(word[prefix_index:])

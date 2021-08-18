from datasketch import MinHash, MinHashLSHForest


class LSHGraph:
    """
    LSH Graph Model
    """

    def __init__(self, df, model, features,
                 id_col="id", n_perm=10):
        """
        :param df: Dataframe containing features of users
        :param model: MinHashLSHForest model
        :param features: Features in the dataset
        :param id_col: User ID column
        :param n_perm: Number of permutations for the LSH model
        """
        self.df = df
        self.model = model
        self.features = features
        self.id_col = id_col
        self.n_perm = n_perm

    def update_graph(self):
        """
        Method to update the LSH graph
        """
        for i, row in self.df[self.features].iterrows():
            if i % 5000 == 0:
                print(f"Processing {i} of {self.df.shape[0]}")
            m = MinHash(num_perm=self.n_perm)
            m = self.get_hash(m, row)
            self.model.add(self.df[self.id_col][i], m)
        self.model.index()

    def extract_neighbors(self, seed, k=10):
        """
        :param seed: List of customer IDs from the seed set
        :param k: Number of neighbors required for each seed set user
        :return: List of neighbors of seed set users
        """
        neighbors = []
        seed_df = self.df[self.df[self.id_col].isin(seed)]
        for i, row in seed_df[self.features].iterrows():
            m = MinHash(num_perm=self.n_perm)
            m = self.get_hash(m, row)
            neighbors.extend(self.model.query(m, k))
        neighbors = list(set(neighbors)-set(seed))
        return neighbors

    def get_hash(self, m, row):
        """
        Function to encode user record using MinHash
        """
        for d in row:
            if type(d) == list:
                for e in d:
                    m.update(str(e).encode('utf-8'))
            else:
                m.update(str(d).encode('utf-8'))
        return m

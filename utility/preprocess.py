from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split # To split the data into training and test set


class PProc:

    @classmethod
    def get_train_test(cls, X, y, test_size=0.3, random_state = 1):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = random_state)

        return X_train, X_test, y_train, y_test
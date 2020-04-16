import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User{1}")

        # # Create friendships

        target_friendships = num_users * avg_friendships // 2
        total_ships = 0
        collisions = 0

        while total_ships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_ships += 1

            else: collisions += 1 
        
        print(f"Total collisions: {collisions}")
        # possible_ships = []

        # for user_id in self.users:
        #     for friend_id in range(user_id+1, self.last_id+1):
        #         possible_ships.append((user_id, friend_id))

        # random.shuffle(possible_ships)

        # for i in range(num_users*avg_friendships // 2):
        #     friendship = possible_ships[i]
        #     self.add_friendship(friendship[0], friendship[1])



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  

        queue = Queue()
        queue.enqueue([user_id])

        while queue.size() > 0:
            current_path = queue.dequeue()
            if not visited.get(current_path[-1], None):
                visited[current_path[-1]] = current_path
                
                for next_friend in self.friendships[current_path[-1]]:
                    new_path = list(current_path)
                    new_path.append(next_friend)
                    queue.enqueue(new_path)
                    
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f'~~~~\nNetwork: {sg.friendships}\n')
    connections = sg.get_all_social_paths(1)

    print(f'~~~~\nConnections: {connections}\n')

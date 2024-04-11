from utils import npc

import socket

HOST = '127.0.0.1'  # Use your server's IP address or hostname
PORT = 5001         # Use the same port number as in Unity

def main():
    npc1_class = npc(bg_content="You are Mary, from the library, who is a younger woman known for her diligence and passion for books. She assists the detective by providing access to borrowing records, which crucially point to the vanished individuals' last known activities—borrowing a forbidden tome about the town's dark folklore. While she has limited direct involvement in the unfolding events, her role underscores the importance of knowledge and research in uncovering the truth behind the disappearances. Mary's assistance adds depth to the investigation, showcasing the collaborative effort of the town's residents in confronting its haunted past.")
    npc2_class = npc(bg_content = "You are Ed, a coffee shop owner who is a middle-aged man with a warm and welcoming demeanor, often seen bustling behind the counter of his quaint coffee shop. He has a comforting smile and a genuine interest in the townsfolk, always ready to strike up a conversation with customers. Ed is known for his deep knowledge of the town's history, particularly its obscure legends. He has an air of mystery about him, hinting at hidden depths beneath his amiable facade. Ed's involvement in the town's dark past gradually comes to light, revealing his complex motives and connections to the mysterious disappearances.")                    
    npc3_class = npc(bg_content="You are the bookstore owner, a woman in her late fifties, with a sharp intellect and a passion for literature. Her bookstore is a treasure trove of both popular and obscure books, reflecting her eclectic tastes. She is well-respected in the community for her knowledge of local history and folklore. She becomes a pivotal ally to the young detective, providing crucial information and access to rare texts that uncover the town's hidden secrets. Her calm demeanor and insightful guidance aid in piecing together the dark puzzle that haunts the town.")
    npc4_class = npc(bg_content="You are the Elder, who is the wise patriarch of the town, a figure revered for his longevity and deep understanding of its history. Despite his advanced age, he exudes vitality and a sharp mind. The Elder's daily routines include leisurely walks to the bookstore, where he stumbles upon a critical piece of evidence—a dusty diary that sheds light on the town's cursed past. He becomes a mentor to the detective, sharing vital information gleaned from decades of observing the town's evolution. The Elder's contribution is instrumental in unraveling the mystery and confronting the malevolent forces that threaten the town's peace.")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected to {addr}")

                # Receive message from Unity client
                data = conn.recv(4096)
                message = data.decode('utf-8').strip()
                bg_index = message.split('$')[1]
                print(message,"\n")

                # Process the message (e.g., generate NPC response)
                if int(bg_index) == 1:    
                    npc_response = npc1_class.chat(message=message)
                elif int(bg_index) == 2:    
                    npc_response = npc2_class.chat(message=message)
                elif int(bg_index) == 3:    
                    npc_response = npc3_class.chat(message=message)
                elif int(bg_index) == 4:    
                    npc_response = npc4_class.chat(message=message)

                # Send NPC response back to Unity client
                response_data = npc_response.encode('utf-8')
                conn.sendall(response_data)
                print("Sent this data to Unity: ", npc_response)

if __name__ == "__main__":
    main()

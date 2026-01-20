from rps.game import Move, play_round


def main():
    print("\nRock • Paper • Scissors\n")

    while True:
        choice = input("Choose rock (r), paper (p), scissors (s), or quit (q): ").lower()

        if choice in {"q", "quit"}:
            print("Goodbye!")
            break

        move = Move.from_user_input(choice)
        if not move:
            print("Invalid choice.\n")
            continue

        result = play_round(move)
        print(
            f"You: {result.player.value} | "
            f"Computer: {result.computer.value} → "
            f"{result.outcome.value.upper()}\n"
        )


if __name__ == "__main__":
    main()

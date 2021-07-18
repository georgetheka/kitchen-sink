import random
import time

from subprocess import Popen

# adjust tempo here
tempo = 90

lookup = {
    'C': 'c',
    'D': 'd',
    'E': 'e',
    'F': 'f',
    'G': 'g',
    'A': 'hey',
    'B': 'b',
    'Bb': 'b flat',
    'Eb': 'e flat',
    'Ab': 'hey flat',
    'Db': 'd flat',
    'Gb': 'g flat',
    'C#': 'c sharp',
    'F#': 'f sharp',
}

pop_sound = '/System/Library/Sounds/Pop.aiff'
tink_sound = '/System/Library/Sounds/Tink.aiff'

notes = list(lookup.keys())

quarter_note_duration_seconds = 60.0 / tempo
measure_quarter_notes = 4

min_num_measures = 4
max_num_measures = 4

# Process
p = None


def speak(text: str) -> None:
    p = Popen(['say', text])


def metronome_sound(path: str) -> None:
    Popen(['afplay', path])


def rand_note() -> str:
    return notes[random.randint(0, len(notes) - 1)]


def main():
    keys = [rand_note()]
    i = 1
    while i < 101:
        # print new key
        n = rand_note()
        # skip consecutive identical keys
        if keys[i - 1] != n:
            keys.append(n)
            i += 1

    for idx, k in enumerate(keys[:100]):
        measures = random.randint(min_num_measures, max_num_measures)
        # print new key
        print(f'<{k}> ({measures})')
        speak(lookup[k])

        for m in range(1, measures + 1):
            if m == measures - 1:
                next_key = keys[idx + 1]
                next_key_spoken = lookup[next_key]
                speak(f'next key is {next_key_spoken}')
                print(f'The next key is {next_key}....')
            print(f'Measure {m}')
            for q in range(0, measure_quarter_notes):
                metronome_sound(pop_sound if q > 0 else tink_sound)
                print(f'* {q + 1}')
                time.sleep(quarter_note_duration_seconds)

    if p:
        p.terminate()


if __name__ == '__main__':
    main()

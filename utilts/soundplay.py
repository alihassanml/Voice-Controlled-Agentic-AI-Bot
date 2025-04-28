import subprocess
import cv2
import playsound


def synthesize_with_piper(text, model_path, output_path="output.mp4"):
    command = [
        "./piper/piper", 
        "--model", model_path,
        "--output_file", output_path
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    process.communicate(input=text.encode())


def main():
    synthesize_with_piper(
        "Hello, I am Ali Hassan and i am a good boy",
        "./piper/en_US-ryan-high.onnx"
    )
    playsound.playsound('output.mp4')

if __name__ == '__main__':
    main()
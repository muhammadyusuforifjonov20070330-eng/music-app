import shutil
import uuid
import os


def save_file(file):
    UPLOAD_DIR = 'audio'

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    audio_ext = ('mp3', 'wav', 'ogg', 'm4a')

    file.file.seek(0, os.SEEK_END)
    file.size = file.file.tell()
    file.file.seek(0)

    if not file.filename.lower().endswith(audio_ext):
        return {'error': 'Fayl audio emas'}
    elif file.size > 16 * 1024 * 1024:
        return {'error': 'Fayl hajmi 16 mb dan oshmasin'}
    else:
        fayl_nomi = file.filename
        ext = fayl_nomi.split('.')[-1]
        new_name = f"{uuid.uuid4()}.{ext}"

        with open(f"{UPLOAD_DIR}/{new_name}", "wb") as rasm:
            shutil.copyfileobj(file.file, rasm)

        return {
            'message': 'Audio muvaffaqiyatli yuklandi',
            'filename': new_name
        }

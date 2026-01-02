import json

class HashExtractorDemo:
    def __init__(self):
        self.hash_formats = {'md5': '$1$', 'sha512': '$6$', 'bcrypt': '$2$'}
    
    def generate_demo_hashes(self):
        return {'shadow_hashes': ['root:hash1', 'admin:hash2'], 'sam_hashes': ['Admin:hash3']}
    
    def export_hashes_json(self, hashes, filename):
        with open(filename, 'w') as f:
            json.dump(hashes, f, indent=4)

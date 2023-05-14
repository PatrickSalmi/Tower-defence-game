class Buttons():

    def __init__(self, x, y, image=None, alt_img=None, text=None):
        self.image = image
        self.alt_img = alt_img
        self.text = text

        if self.image:
            self.alt = False
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def draw(self, display):
        if not self.alt:
            display.blit(self.image, self.rect)
        else:
            display.blit(self.alt_img, self.rect)

from data.scripts.core_funcs import *

global e_colorkey
e_colorkey = (255, 255, 255)


def set_global_colorkey(colorkey):
    global e_colorkey
    e_colorkey = colorkey


KNOWN_TAGS = ['loop']


# entity stuff
def simple_entity(x, y, e_type):
    return Entity(x, y, 1, 1, e_type)


def flip(img, boolean=True, boolean_2=False):
    return pygame.transform.flip(img, boolean, boolean_2)


def blit_center(surf, surf2, pos):
    x = int(surf2.get_width() / 2)
    y = int(surf2.get_height() / 2)
    surf.blit(surf2, (pos[0] - x, pos[1] - y))


class Entity(object):
    global animation_database, animation_higher_database

    def __init__(self, x, y, width, height, e_type):
        self.x = x
        self.y = y
        self.original_y = y
        self.original_x = x
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.animation = None
        self.image = None
        self.animation_frame = 0
        self.animation_tags = []
        self.flip = False
        self.offset = [0, 0]
        self.rotation = 0
        self.type = e_type  # used to determine animation set among other things
        self.action_timer = 0
        self.current_action = ''
        self.set_action('idle')  # overall action for the entity
        self.entity_data = {}
        self.alpha = None
        self.animation_progress = 0

    def set_pos(self, loc):
        x = loc[0]
        y = loc[1]
        self.x = x
        self.y = y

    def update_variable(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def set_flip(self, boolean):
        self.flip = boolean

    def set_animation_tags(self, tags):
        self.animation_tags = tags

    def set_animation(self, sequence):
        self.animation = sequence
        self.animation_frame = 0

    def set_action(self, action_id, force=False):
        pass

    def get_entity_angle(self, entity_2):
        x1 = self.x + int(self.width / 2)
        y1 = self.y + int(self.height / 2)
        x2 = entity_2.x + int(entity_2.width / 2)
        y2 = entity_2.y + int(entity_2.height / 2)
        angle = math.atan((y2 - y1) / (x2 - x1))
        if x2 < x1:
            angle += math.pi
        return angle

    def get_point_angle(self, point):
        return math.atan2(point[1] - self.get_center()[1], point[0] - self.get_center()[0])

    def get_distance(self, point):
        dis_x = point[0] - self.get_center()[0]
        dis_y = point[1] - self.get_center()[1]
        return math.sqrt(dis_x ** 2 + dis_y ** 2)

    def get_center(self):
        x = self.x + int(self.width / 2)
        y = self.y + int(self.height / 2)
        return [x, y]

    def clear_animation(self):
        self.animation = None

    def set_image(self, image):
        self.image = image

    def set_offset(self, offset):
        self.offset = offset

    def set_frame(self, amount):
        self.animation_frame = amount

    def handle(self):
        self.action_timer += 1
        self.change_frame(1)

    def change_frame(self, amount):
        self.animation_frame += amount
        if self.animation is not None:
            while self.animation_frame < 0:
                if 'loop' in self.animation_tags:
                    self.animation_frame += self.animation
                else:
                    self.animation = 0
            while self.animation_frame >= self.animation:
                if 'loop' in self.animation_tags:
                    self.animation_frame -= self.animation
                else:
                    self.animation_frame = self.animation - 1
                    for tag in self.animation_tags:
                        if tag not in KNOWN_TAGS:
                            self.set_action(tag)
            self.animation_progress = (self.animation_frame + 1) / self.animation

    def get_current_img(self):
        if self.animation is None:
            if self.image is not None:
                return flip(self.image, self.flip)
            else:
                return None
        else:
            return flip(animation_database[self.animation[self.animation_frame]], self.flip)

    def get_drawn_img(self):
        image_to_render = None
        if self.animation is None and self.image is not None:
            image_to_render = flip(self.image, self.flip).copy()
        else:
            image_to_render = flip(animation_database[self.animation[self.animation_frame]], self.flip).copy()
        if image_to_render is not None:
            center_x = image_to_render.get_width() / 2
            center_y = image_to_render.get_height() / 2
            image_to_render = pygame.transform.rotate(image_to_render, self.rotation)
            if self.alpha is not None:
                image_to_render.set_alpha(self.alpha)
            return image_to_render, center_x, center_y

    def display(self, surface, scroll):
        image_to_render = None
        if self.animation is None:
            if self.image is not None:
                image_to_render = flip(self.image, self.flip).copy()
        else:
            image_to_render = flip(animation_database[self.animation[self.animation_frame]], self.flip).copy()
        if image_to_render is not None:
            center_x = image_to_render.get_width() / 2
            center_y = image_to_render.get_height() / 2
            image_to_render = pygame.transform.rotate(image_to_render, self.rotation)
            if self.alpha is not None:
                image_to_render.set_alpha(self.alpha)
            blit_center(surface, image_to_render, (int(self.x) - scroll[0] + self.offset[0] + center_x,
                                                   int(self.y) - scroll[1] + self.offset[1] + center_y))


# animation stuff

global animation_database
animation_database = {}

global animation_higher_database
animation_higher_database = {}


# a sequence looks like [[0,1],[1,1],[2,1],[3,1],[4,2]]
# the first numbers are the image name(as integer), while the second number shows the duration of it in the sequence
def animation_sequence(sequence, base_path, colorkey=(255, 255, 255), transparency=255):
    global animation_database
    result = []
    for frame in sequence:
        image_id = base_path + base_path.split('/')[-2] + '_' + str(frame[0])
        image = pygame.image.load(image_id + '.png').convert()
        image.set_colorkey(colorkey)
        image.set_alpha(transparency)
        animation_database[image_id] = image.copy()
        for _ in range(frame[1]):
            result.append(image_id)
    return result


def get_frame(frame_id):
    global animation_database
    return animation_database[frame_id]


def load_animations2(path):
    pass


# particles
def particle_file_sort(l):
    l2 = []
    for obj in l:
        l2.append(int(obj[:-4]))
    l2.sort()
    l3 = []
    for obj in l2:
        l3.append(str(obj) + '.png')
    return l3


global particle_images
particle_images = {}


def load_particle_images(path):
    pass


class Particle(object):
    def __init__(self, x, y, particle_type, motion, decay_rate, start_frame, custom_color=None, physics=False):
        self.x = x
        self.y = y
        self.type = particle_type
        self.motion = motion
        self.decay_rate = decay_rate
        self.color = custom_color
        self.frame = start_frame
        self.physics = physics
        self.orig_motion = self.motion
        self.temp_motion = [0, 0]
        self.time_left = len(particle_images[self.type]) + 1 - self.frame
        self.render = True

    def draw(self, surface, scroll):
        global particle_images
        if self.render:
            if self.color is None:
                blit_center(surface, particle_images[self.type][int(self.frame)],
                            (self.x - scroll[0], self.y - scroll[1]))
            else:
                blit_center(surface,
                            swap_color(particle_images[self.type][int(self.frame)], (255, 255, 255), self.color),
                            (self.x - scroll[0], self.y - scroll[1]))

    def update(self, dt):
        self.frame += self.decay_rate * dt
        self.time_left = len(particle_images[self.type]) + 1 - self.frame
        running = True
        self.render = True
        if self.frame >= len(particle_images[self.type]):
            self.render = False
            if self.frame >= len(particle_images[self.type]) + 1:
                running = False
        if not self.physics:
            self.x += (self.temp_motion[0] + self.motion[0]) * dt
            self.y += (self.temp_motion[1] + self.motion[1]) * dt
        self.temp_motion = [0, 0]
        return running


# other useful functions

def swap_color(img, old_c, new_c):
    global e_colorkey
    img.set_colorkey(old_c)
    surf = img.copy()
    surf.fill(new_c)
    surf.blit(img, (0, 0))
    surf.set_colorkey(e_colorkey)
    return surf

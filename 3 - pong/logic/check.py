def hi():
    print('hi')

def close(pygame):
    pygame.quit()
    return False

def select(event,pygame):
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        return -1
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        return 1
    return 0
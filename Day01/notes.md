task-01: No error

task-02:
    1. Increment count in each iteration.
    2. Create the target directory before saving

task-03: 
    A-> Share code
    B-> fourcc is four character code
    C. after loading, the image files haven't been sorted. Sort them Just add a "image_files.sort()" after the "if not image_files" condition
    D. in task-2, in the cv2.imwrite line, use "cv2.imwrite(f"../data/01_IO/vid_frames/{count:04d}.jpg", frame)"


task-04:
    line 14 & 15, have messed up the selection of which frames to use (We have to use first 15 and last 15. While the code ignores the first and last 15 and uses all others)

task-05: No error

task-06:
    A. Replace "img=1" with img = np.full((300, 300), 127); img[:, 100:200] = 255
    B. set dtype as 'uint8' to resolve the error
    C. Use cmap='gray' in matplotlib
    D. If matplotlib is not displaying the colour properly, set any one pixel in matlplotlib to be 0. Then it will work.

task-07:
    line-15: Replace "/" by "//" to fix the bug

task-08: 
    Define the gamma transform function as below
    C = 255**(1-gamma)
    return C * (img**gamma)

General
    Change the data directory format many times
    use inline matlplotlib in colab
    - Share task-11 code or not ?
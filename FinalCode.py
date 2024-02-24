import cv2
import numpy as np

# extracts principle points and focal lengths
intrinsics = np.load('intrinsics.npy',allow_pickle=True)
world_coordinates = np.load('world_coordinates.npy',allow_pickle=True)
image = cv2.imread("image.jpg")

# Selects minimum six pixel cordinates
height,width,_=image.shape
pixel_coordinates = []
def mouse_click(event, x,y, flags, parameter):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel_coordinates.append([x,y])
    
cv2.namedWindow("Image")
cv2.setMouseCallback("Image",mouse_click)    
while True:
    cv2.imshow("Image",image)
    key = cv2.waitKey(1) & 0xFF
    if key == 13:
        break

# Maps each 2D pixel coordinates to the corresponding 3D coordinate in the world frame
world_points = []
for x, y in pixel_coordinates:
    if 0<=y < world_coordinates.shape[0] and 0<=x < world_coordinates.shape[1]:
        world_points.append(world_coordinates[y, x])

# Changes coordinates into [x,y,z] form
new_world_points = []
for i in world_points:
    new_world_points.append(i[:3]) 

# Rounds off each coordinate to 5 decimal places
for i in new_world_points:
    for x in range(len(i)):
        i[x] = round(i[x],5)

new_world_points_edit = []
for i in new_world_points:
    new_world_points_edit.append(list(i))

# Sets up the camera matrix
intrinsics_new = intrinsics.tolist()
fx,fy,cx,cy=intrinsics_new["fx"],intrinsics_new["fy"],intrinsics_new["ppx"],intrinsics_new["ppy"] 
camera_matrix = np.array([[fx, 0, cx],
                        [0, fy, cy],
                           [0, 0, 1]],dtype = np.float32)

# Computes the rotational and the translational vector
if len(new_world_points_edit) < 6:
    print("Minumum six points required")
else:
    retval, rot_vector, trans_vector = cv2.solvePnP(np.array(new_world_points_edit,dtype = np.float32), np.array(pixel_coordinates,dtype = np.float32),camera_matrix, distCoeffs=None, flags=cv2.SOLVEPNP_ITERATIVE,useExtrinsicGuess=False)
    print("Rotational Vector: ",rot_vector)
    print("Translational Vector: ",trans_vector)

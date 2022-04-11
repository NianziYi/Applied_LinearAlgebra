fprintf('Part A \n');
%Initialize time t (seconds) and the horizontal position of the plane (feet) given the data.
t=0:12;
y=[0;8.8;29.9;62.0;104.7;159.1;222.0;294.5;380.4;471.1;571.7;686.8;809.2];

%Populate a 13x4 matrix A since there are 13 t values and 4 β values (β0,β1,β2,β4).
A=zeros(13,4);
A(:,1)=ones(13,1);
A(:,2)=t;
A(:,3)=t.^2;
A(:,4)=t.^3;

%Use polyfit() to find the coefficients for a polynomial of degree 3 that is a best fit for the data in y (aka βeta coefficients of y).
beta=polyfit(t,y,3);
beta
fprintf('The least-squares cubic curve y = β0 + β1t + β2t^2 + β3t^3 for these data is \n');
fprintf('y = (%.4f) + (%.4f)*t + (%.4f)*t^2 + (%.4f)*t^3\n', beta)
fprintf('\n');

fprintf('Part B \n');
%Use polyder() to take the derivative of y in order to obtain the velocity curve.
velocity_curve=polyder(beta);

%Use polyval() to find the velocity of the plane when time t = 4.5 seconds.
velocity=polyval(velocity_curve,4.5);
fprintf('The estimated velocity of the plane when t = 4.5 seconds is %f ft/sec.\n', velocity)
fprintf('\n');

fprintf('Part C \n');
%Initialize the diagonal weighting matrix W with given diagonal entries.
W=diag([1, 1, 1, 0.9, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]);

% A is the design matrix.
A=[[1 0 0 0];
   [1 1 1 1];
   [1 2 4 8];
   [1 3 9 27];
   [1 4 16 64];
   [1 5 25 125];
   [1 6 36 216];
   [1 7 49 343];
   [1 8 64 512];
   [1 9 81 729];
   [1 10 100 1000];
   [1 11 121 1331];
   [1 12 144 1728]];

% y transpose is the observation vector.
y=[0 8.8 29.9 62.0 104.7 159.1 222.0 294.5 380.4 471.1 571.7 686.8 809.2]'; % y transpose

% Get weighted A and y values with the diagonal weighting matrix W taken in account.
weighted_A = W*A;
weighted_y = W*y;
weightedAtranspose_weightedA = ((W*A)')*(W*A);
weightedytranspose_weightedy = ((W*A)')*(W*y);

% Use inv() to find the new β coefficients of y.
weighted_beta = inv(weightedAtranspose_weightedA)'*weightedytranspose_weightedy;
weighted_beta
fprintf('The weighted least-squares cubic curve is \n');
fprintf('y = (%.4f) + (%.4f)*t + (%.4f)*t^2 + (%.4f)*t^3\n', weighted_beta);

% Use diff() to take the derivative of y in order to obtain the velocity curve 
syms t
y = (-0.2685) + (3.6095)*t + (5.8576)*t^2 + (-0.0477)*t^3;
weighted_velocity_curve = diff(y);
weighted_velocity_curve

% Use subs() to replace 4.5 with t to get the velocity of the plane when time t = 4.5 seconds.
t=4.5;
weighted_velocity = subs(weighted_velocity_curve)
fprintf('The estimated velocity of the plane when t = 4.5 seconds is %f ft/sec.\n', weighted_velocity)
#include <iostream>
#include <Eigen/Dense>
#include <Eigen/QR>

using Eigen::MatrixXd;

int main()
{
  float c = 343.0;
  MatrixXd array_geom(4,3);
  array_geom << 0,0,0, 0,1,0, 1,0,0, 0,0,1;
  VectorXf d, tau;
  d << 0.01, 0.2, -0.3;
  tau = d/c;
  std::cout << tau << "tau" <<std::endl;

  MatrixXd R = array_geom.block(1,0, array_geom.rows()-1, array_geom.cols());
  Vector

  std::cout <<array_geom << std::endl;
  std::cout << "yaay" << std::endl;
  std::cout << R << std::endl;
  // performing a pseudo-inverse. Not the 'recommended way' - but wtf, it works right now...
  std::cout<< "\n" << "pseudoinverse of R" << std::endl;
  Eigen::MatrixXd pinv = R.completeOrthogonalDecomposition().pseudoInverse();
  std::cout << pinv << '\n';
  return 0;
  
}